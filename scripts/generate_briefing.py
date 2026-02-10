#!/usr/bin/env python3
"""
Elixirr AI Transformation Executive Briefing Generator

Reads a JSON config file and generates a branded PDF briefing.

Usage:
    python generate_briefing.py <config.json> <output.pdf>

Config JSON structure:
{
  "prospect": {
    "name": "First Last",
    "title": "Chief Executive Officer",
    "company": "Company Name",
    "short_title": "CEO"
  },
  "cover": {
    "main_title_line1": "AI Transformation",
    "main_title_line2": "in [Industry]",
    "subtitle_line1": "A strategic briefing on ...",
    "subtitle_line2": "... second line."
  },
  "sections": [
    {
      "title": "Section Title",
      "subtitle": "Section subtitle text",
      "elements": [
        {"type": "intro", "text": "Bold intro paragraph"},
        {"type": "body", "text": "Normal body paragraph"},
        {"type": "heading", "text": "Sub-heading text"},
        {"type": "numbered", "number": 1, "title": "TITLE", "body": "Description"},
        {"type": "insight", "text": "Callout text", "style": "warm|cool"},
        {"type": "table", "headers": ["Col1","Col2","Col3"],
         "rows": [["cell","cell","cell"]]},
        {"type": "spacer", "height": 10},
        {"type": "page_break"}
      ]
    }
  ]
}
"""

import json
import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable, Frame, PageTemplate, BaseDocTemplate, NextPageTemplate
)
from reportlab.platypus.flowables import Flowable

# ─── Elixirr Brand Colors ───
DARK_PLUM = HexColor("#2B1B4E")
ACCENT_AMBER = HexColor("#E8A832")
ACCENT_CORAL = HexColor("#E87850")
LIGHT_LAVENDER = HexColor("#F0ECF5")
MEDIUM_PURPLE = HexColor("#6B5B8A")
WARM_GRAY = HexColor("#F5F5F3")
TEXT_DARK = HexColor("#1A1A2E")
TEXT_MEDIUM = HexColor("#4A4A5A")
TEXT_LIGHT = HexColor("#6B7280")
BORDER_LIGHT = HexColor("#D1D5DB")
WHITE = white


# ─── Custom Flowables ───

class AccentLine(Flowable):
    def __init__(self, width, color=ACCENT_AMBER, thickness=2):
        Flowable.__init__(self)
        self.width = width
        self.color = color
        self.thickness = thickness
        self.height = thickness + 4

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 2, self.width, 2)


class InsightBox(Flowable):
    def __init__(self, text, width, style="cool"):
        Flowable.__init__(self)
        self.text = text
        self.box_width = width
        if style == "warm":
            self.accent_color = ACCENT_CORAL
            self.bg_color = HexColor("#FDF0EC")
        else:
            self.accent_color = DARK_PLUM
            self.bg_color = LIGHT_LAVENDER

        text_style = ParagraphStyle('IB', fontName='Helvetica-Oblique',
                                     fontSize=10, leading=15, textColor=TEXT_DARK)
        p = Paragraph(self.text, text_style)
        w, h = p.wrap(self.box_width - 30, 1000)
        self.box_height = h + 20
        self.height = self.box_height + 8

    def draw(self):
        c = self.canv
        c.setFillColor(self.bg_color)
        c.roundRect(0, 0, self.box_width, self.box_height, 3, fill=1, stroke=0)
        c.setFillColor(self.accent_color)
        c.rect(0, 0, 4, self.box_height, fill=1, stroke=0)

        text_style = ParagraphStyle('IBD', fontName='Helvetica-Oblique',
                                     fontSize=10, leading=15, textColor=TEXT_DARK)
        p = Paragraph(self.text, text_style)
        p.wrap(self.box_width - 30, 1000)
        p.drawOn(c, 18, 10)


class NumberedPoint(Flowable):
    def __init__(self, number, title, body, width, number_color=DARK_PLUM):
        Flowable.__init__(self)
        self.number = str(number)
        self.title = title
        self.body = body
        self.total_width = width
        self.number_color = number_color

        title_style = ParagraphStyle('NPT', fontName='Helvetica-Bold',
                                      fontSize=11, leading=14, textColor=TEXT_DARK)
        body_style = ParagraphStyle('NPB', fontName='Helvetica',
                                     fontSize=10, leading=15, textColor=TEXT_MEDIUM, spaceAfter=4)
        text_width = self.total_width - 40
        tp = Paragraph(self.title, title_style)
        tw, th = tp.wrap(text_width, 1000)
        bp = Paragraph(self.body, body_style) if self.body else None
        bh = 0
        if bp:
            bw, bh = bp.wrap(text_width, 1000)
        self.height = max(th + bh + 8, 30) + 4

    def draw(self):
        c = self.canv
        c.setFillColor(self.number_color)
        c.circle(14, self.height - 14, 12, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(14, self.height - 18, self.number)

        text_width = self.total_width - 40
        title_style = ParagraphStyle('NPTD', fontName='Helvetica-Bold',
                                      fontSize=11, leading=14, textColor=TEXT_DARK)
        body_style = ParagraphStyle('NPBD', fontName='Helvetica',
                                     fontSize=10, leading=15, textColor=TEXT_MEDIUM)

        tp = Paragraph(self.title, title_style)
        tw, th = tp.wrap(text_width, 1000)
        tp.drawOn(c, 36, self.height - th - 2)

        if self.body:
            bp = Paragraph(self.body, body_style)
            bw, bh = bp.wrap(text_width, 1000)
            bp.drawOn(c, 36, self.height - th - bh - 6)


# ─── Logo Handling ───

def _get_default_logo_path():
    """Get the default logo path relative to this script's location."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, '..', 'assets', 'elixirr-logo.png')


def draw_elixirr_logo(c, x_center, y_bottom, width, logo_path=None):
    """Draw the Elixirr logo image centered at x_center, with bottom at y_bottom."""
    if logo_path is None:
        logo_path = _get_default_logo_path()
    if not os.path.exists(logo_path):
        # Fallback: draw text if logo file not found
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 22)
        c.drawCentredString(x_center, y_bottom + 10, "E L I X I R R")
        return
    logo = ImageReader(logo_path)
    iw, ih = logo.getSize()
    aspect = ih / iw
    height = width * aspect
    x = x_center - width / 2
    c.drawImage(logo, x, y_bottom, width=width, height=height, mask='auto')


# ─── Page Templates ───

class BriefingDoc:
    """Manages the document generation from config."""

    def __init__(self, config, output_path):
        self.config = config
        self.output_path = output_path
        self.prospect = config["prospect"]
        self.cover = config["cover"]
        self.sections = config["sections"]
        self.w, self.h = letter
        self.margin_left = 60
        self.margin_right = 60
        self.content_width = self.w - self.margin_left - self.margin_right

    def _cover_page(self, canvas_obj, doc):
        c = canvas_obj
        w, h = self.w, self.h

        c.setFillColor(DARK_PLUM)
        c.rect(0, 0, w, h, fill=1, stroke=0)

        c.setFillColor(HexColor("#33205A"))
        c.rect(0, h - 200, w, 200, fill=1, stroke=0)

        # Draw the real Elixirr logo (swoosh + wordmark), centered in top band
        logo_path = self.config.get("logo_path") or _get_default_logo_path()
        logo_width = 300
        # Center vertically in the 200pt top band
        # Logo aspect ≈ 105/600 = 0.175, so height ≈ 52.5pt
        logo_height = logo_width * 0.175
        logo_y = h - 200 + (200 - logo_height) / 2
        draw_elixirr_logo(c, w/2, logo_y, logo_width, logo_path)

        c.setStrokeColor(ACCENT_AMBER)
        c.setLineWidth(2)
        c.line(60, h - 200, w - 60, h - 200)

        c.setFillColor(ACCENT_AMBER)
        c.setFont('Helvetica', 10)
        c.drawString(60, h - 232, "PREPARED FOR")

        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 26)
        c.drawString(60, h - 268, self.prospect["name"])

        c.setFont('Helvetica', 14)
        c.setFillColor(HexColor("#B8A0D0"))
        c.drawString(60, h - 296, f"{self.prospect['title']}  |  {self.prospect['company']}")

        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 32)
        y = h - 390
        c.drawString(60, y, self.cover["main_title_line1"])
        c.drawString(60, y - 40, self.cover["main_title_line2"])

        c.setFont('Helvetica', 14)
        c.setFillColor(HexColor("#B8A0D0"))
        c.drawString(60, y - 82, self.cover["subtitle_line1"])
        c.drawString(60, y - 100, self.cover["subtitle_line2"])

        c.setStrokeColor(ACCENT_AMBER)
        c.setLineWidth(1)
        c.line(60, 130, w - 60, 130)

        c.setFillColor(HexColor("#9080AA"))
        c.setFont('Helvetica', 9)
        c.drawString(60, 108, "PREPARED BY")
        c.setFillColor(HexColor("#D0C0E0"))
        c.setFont('Helvetica-Bold', 11)
        c.drawString(60, 91, "Adam Hofmann")
        c.setFont('Helvetica', 10)
        c.setFillColor(HexColor("#B8A0D0"))
        c.drawString(60, 75, "Elixirr Partner \u2014 AI")
        c.setFont('Helvetica', 9)
        c.setFillColor(HexColor("#9080AA"))
        c.drawString(60, 60, "adam.hofmann@elixirr.com  |  +1-415-636-1620")

        c.setFillColor(HexColor("#9080AA"))
        c.setFont('Helvetica', 9)
        import datetime
        month_year = datetime.datetime.now().strftime("%B %Y").upper()
        c.drawRightString(w - 60, 108, month_year)

    def _body_page(self, canvas_obj, doc):
        c = canvas_obj
        w, h = self.w, self.h
        name_upper = self.prospect["name"].upper()
        company_upper = self.prospect["company"].upper()

        c.setFillColor(DARK_PLUM)
        c.rect(0, h - 28, w, 28, fill=1, stroke=0)

        c.setFillColor(HexColor("#B8A0D0"))
        c.setFont('Helvetica', 7.5)
        c.drawString(60, h - 20,
                     f"AI TRANSFORMATION BRIEFING  |  {name_upper}  |  {company_upper}")

        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 7.5)
        c.drawRightString(w - 60, h - 20, "E L I X I R R")

        c.setStrokeColor(HexColor("#D1C5E0"))
        c.setLineWidth(0.5)
        c.line(60, 45, w - 60, 45)

        c.setFillColor(TEXT_LIGHT)
        c.setFont('Helvetica', 8)
        c.drawCentredString(w / 2, 30, str(doc.page))

        c.setFont('Helvetica', 6.5)
        c.drawString(60, 30, "CONFIDENTIAL")

    def _build_styles(self):
        self.styles = {
            "section_title": ParagraphStyle(
                'SectionTitle', fontName='Helvetica-Bold', fontSize=20,
                leading=26, textColor=DARK_PLUM, spaceBefore=0, spaceAfter=6),
            "section_subtitle": ParagraphStyle(
                'SectionSubtitle', fontName='Helvetica', fontSize=11,
                leading=16, textColor=TEXT_LIGHT, spaceBefore=0, spaceAfter=16),
            "heading": ParagraphStyle(
                'Heading2', fontName='Helvetica-Bold', fontSize=13,
                leading=18, textColor=DARK_PLUM, spaceBefore=18, spaceAfter=8),
            "body": ParagraphStyle(
                'BodyText', fontName='Helvetica', fontSize=10,
                leading=15.5, textColor=TEXT_MEDIUM, spaceBefore=0,
                spaceAfter=8, alignment=TA_JUSTIFY),
            "intro": ParagraphStyle(
                'IntroText', fontName='Helvetica', fontSize=10.5,
                leading=16, textColor=TEXT_DARK, spaceBefore=0,
                spaceAfter=10, alignment=TA_JUSTIFY),
            "closing": ParagraphStyle(
                'Closing', fontName='Helvetica', fontSize=10.5,
                leading=16, textColor=TEXT_DARK, spaceBefore=6, spaceAfter=8),
        }

    def _render_element(self, el, story):
        el_type = el["type"]

        if el_type == "intro":
            story.append(Paragraph(el["text"], self.styles["intro"]))

        elif el_type == "body":
            story.append(Paragraph(el["text"], self.styles["body"]))

        elif el_type == "closing":
            story.append(Paragraph(el["text"], self.styles["closing"]))

        elif el_type == "heading":
            story.append(Paragraph(el["text"], self.styles["heading"]))

        elif el_type == "numbered":
            color = ACCENT_AMBER if el.get("accent") == "gold" else DARK_PLUM
            story.append(NumberedPoint(
                el["number"], el["title"], el.get("body", ""),
                self.content_width, color))
            story.append(Spacer(1, 6))

        elif el_type == "insight":
            style = el.get("style", "cool")
            story.append(InsightBox(el["text"], self.content_width, style))
            story.append(Spacer(1, 8))

        elif el_type == "table":
            self._render_table(el, story)

        elif el_type == "spacer":
            story.append(Spacer(1, el.get("height", 10)))

        elif el_type == "page_break":
            story.append(PageBreak())

        elif el_type == "signature":
            self._render_signature(story)

        elif el_type == "hr":
            story.append(HRFlowable(
                width=self.content_width * 0.3, thickness=1,
                color=BORDER_LIGHT, spaceAfter=12))

    def _render_table(self, el, story):
        headers = el["headers"]
        rows = el["rows"]

        th_style = ParagraphStyle('TH', fontName='Helvetica-Bold',
                                   fontSize=8.5, textColor=WHITE, leading=12)
        tc_bold = ParagraphStyle('TCB', fontName='Helvetica-Bold',
                                  fontSize=9, textColor=TEXT_DARK, leading=13)
        tc_norm = ParagraphStyle('TCN', fontName='Helvetica',
                                  fontSize=9, textColor=TEXT_MEDIUM, leading=13)

        table_data = [[Paragraph(f"<b>{h}</b>", th_style) for h in headers]]

        for row in rows:
            table_row = []
            for i, cell in enumerate(row):
                style = tc_bold if i == 0 else tc_norm
                table_row.append(Paragraph(cell, style))
            table_data.append(table_row)

        num_cols = len(headers)
        col_widths = el.get("col_widths")
        if col_widths:
            col_widths = [self.content_width * w for w in col_widths]
        else:
            col_widths = [self.content_width / num_cols] * num_cols

        table = Table(table_data, colWidths=col_widths, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), DARK_PLUM),
            ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), WHITE),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, WARM_GRAY]),
            ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
            ('LINEBELOW', (0, 0), (-1, 0), 1.5, ACCENT_AMBER),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(table)
        story.append(Spacer(1, 12))

    def _render_signature(self, story):
        story.append(Spacer(1, 20))
        story.append(HRFlowable(
            width=self.content_width * 0.3, thickness=1,
            color=BORDER_LIGHT, spaceAfter=12))

        sig = ParagraphStyle('Sig', fontName='Helvetica', fontSize=10.5,
                              leading=15, textColor=TEXT_DARK)
        sig_d = ParagraphStyle('SigD', fontName='Helvetica', fontSize=10,
                                leading=14, textColor=TEXT_MEDIUM)
        sig_l = ParagraphStyle('SigL', fontName='Helvetica', fontSize=10,
                                textColor=DARK_PLUM, leading=14)

        story.append(Paragraph("<b>Adam Hofmann</b>", sig))
        story.append(Paragraph("Elixirr Partner \u2014 AI", sig_d))
        story.append(Paragraph(
            "adam.hofmann@elixirr.com  |  +1-415-636-1620", sig_l))

    def build(self):
        self._build_styles()

        doc = BaseDocTemplate(
            self.output_path,
            pagesize=letter,
            leftMargin=self.margin_left,
            rightMargin=self.margin_right,
            topMargin=70,
            bottomMargin=65,
            title=f"AI Transformation Briefing - {self.prospect['name']} - {self.prospect['company']}",
            author="Elixirr"
        )

        cover_frame = Frame(self.margin_left, 50, self.content_width,
                            self.h - 100, id='cover')
        body_frame = Frame(self.margin_left, 65, self.content_width,
                           self.h - 140, id='body')

        doc.addPageTemplates([
            PageTemplate(id='Cover', frames=cover_frame,
                         onPage=self._cover_page),
            PageTemplate(id='Body', frames=body_frame,
                         onPage=self._body_page),
        ])

        story = []

        # Cover page
        story.append(NextPageTemplate('Body'))
        story.append(PageBreak())

        # Sections
        for i, section in enumerate(self.sections):
            if i > 0:
                story.append(PageBreak())

            story.append(Paragraph(section["title"],
                                   self.styles["section_title"]))
            story.append(AccentLine(80, ACCENT_AMBER, 2))
            story.append(Spacer(1, 4))

            if section.get("subtitle"):
                story.append(Paragraph(section["subtitle"],
                                       self.styles["section_subtitle"]))

            for el in section.get("elements", []):
                self._render_element(el, story)

        doc.build(story)
        print(f"PDF generated: {self.output_path}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_briefing.py <config.json> <output.pdf>")
        sys.exit(1)

    config_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(config_path, 'r') as f:
        config = json.load(f)

    briefing = BriefingDoc(config, output_path)
    briefing.build()


if __name__ == "__main__":
    main()
