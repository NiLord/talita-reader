import { Component } from '@angular/core';
import { ProcessPdfService } from '../process-pdf.service';

@Component({
  selector: 'app-pdf-update',
  templateUrl: './pdf-update.component.html',
  styleUrls: ['./pdf-update.component.css']
})
export class PdfUpdateComponent {

  firstPDF : any;
  secondPDF : any;
  daysDiference : number = 0;

  constructor(private pdfService: ProcessPdfService) { }

  ngOnInit(): void {
  }

  calcularDiferenciaEnDias(fecha1: string, fecha2: string): number {
    const fechaObj1 = new Date(fecha1);
    const fechaObj2 = new Date(fecha2);
    const diferenciaEnMs = fechaObj2.getTime() - fechaObj1.getTime();
    const diferenciaEnDias = Math.round(diferenciaEnMs / 86400000);
    return diferenciaEnDias;
  }

  // Método que se ejecuta cuando se selecciona un archivo en el formulario
  onFileChange(event: HTMLInputElement) {
    console.log(event)
    if (event.files != null) {
      const file = event.files[0];

      // Creamos un lector de archivos
      const reader = new FileReader();

      // Leemos el archivo como datos de tipo URL
      reader.readAsDataURL(file);

      // Cuando termine de leer, ejecutamos el código que convierte el archivo en base64
      reader.onload = () => {
        // Convertimos el archivo a base64
        const fileBase64 = reader.result;
        if (fileBase64 !== null && fileBase64 !== undefined && typeof fileBase64 === 'string') {
          this.pdfService.obtenerDatos(fileBase64.split(",")[1]).subscribe(resultado => {
            if(event.name === "archivoUno"){
              this.firstPDF = resultado;
            }else{
              this.secondPDF = resultado;
              this.daysDiference = this.calcularDiferenciaEnDias(this.firstPDF?.date, this.secondPDF?.date);
            }
            console.log(resultado);
          });
        }
      };
    }
  }


}
