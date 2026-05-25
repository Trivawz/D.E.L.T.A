from fpdf import FPDF
import datetime

def generate_delta_report(data):
    pdf = FPDF()
    pdf.add_page()
    
    # Tactical Header
    pdf.set_font("Courier", "B", 16)
    pdf.cell(200, 10, txt="PROJECT D.E.L.T.A. | INTEL REPORT", ln=True, align='C')
    pdf.set_font("Courier", "", 10)
    pdf.cell(200, 10, txt=f"TIMESTAMP: {datetime.datetime.now()}", ln=True, align='C')
    pdf.ln(10)
    
    # Body
    pdf.set_font("Courier", "B", 12)
    pdf.cell(200, 10, txt="[ TARGET DATA ]", ln=True)
    pdf.set_font("Courier", "", 12)
    pdf.cell(200, 10, txt=f"LATITUDE:  {data['lat']}", ln=True)
    pdf.cell(200, 10, txt=f"LONGITUDE: {data['lng']}", ln=True)
    pdf.cell(200, 10, txt=f"CONFIDENCE: {data['confidence']}%", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Courier", "B", 12)
    pdf.cell(200, 10, txt="[ ANALYSIS ]", ln=True)
    pdf.set_font("Courier", "", 11)
    pdf.multi_cell(0, 10, txt=data['analysis'])
    
    filename = f"report_{int(datetime.datetime.now().timestamp())}.pdf"
    pdf.output(f"static/{filename}")
    return filename