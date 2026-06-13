import os
from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    ticker,
    fundamental_report,
    quant_report,
    macro_report,
    cio_report
):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{ticker}_Investment_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    # =====================
    # COVER PAGE
    # =====================

    title = Paragraph(
        f"<b>AI Investment Research Report</b>",
        styles["Title"]
    )

    subtitle = Paragraph(
        f"Ticker: {ticker}<br/>"
        f"Generated: {datetime.now()}",
        styles["Normal"]
    )

    elements.append(title)
    elements.append(Spacer(1, 20))
    elements.append(subtitle)
    elements.append(PageBreak())

    # =====================
    # AGENT 1
    # =====================

    elements.append(
        Paragraph(
            "<b>Agent 1 - Fundamental Analysis</b>",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            fundamental_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    elements.append(PageBreak())

    # =====================
    # AGENT 2
    # =====================

    elements.append(
        Paragraph(
            "<b>Agent 2 - Quantitative Analysis</b>",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            quant_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    elements.append(PageBreak())

    # =====================
    # AGENT 3
    # =====================

    elements.append(
        Paragraph(
            "<b>Agent 3 - Macro Risk Analysis</b>",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            macro_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    elements.append(PageBreak())

    # =====================
    # AGENT 4
    # =====================

    elements.append(
        Paragraph(
            "<b>Agent 4 - Chief Investment Officer</b>",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            cio_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(elements)

    print(f"\nPDF Report Generated Successfully:")
    print(filename)

    return filename