import { Component } from '@angular/core';
import { ProcessPdfService } from '../process-pdf.service';

@Component({
  selector: 'app-pdf-update',
  templateUrl: './pdf-update.component.html',
  styleUrls: ['./pdf-update.component.css']
})
export class PdfUpdateComponent {

  constructor(private pdfService: ProcessPdfService) { }

  ngOnInit(): void {
  }

  // Método que se ejecuta cuando se selecciona un archivo en el formulario
  onFileChange(event: HTMLInputElement) {
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
            console.log(resultado);
          });
        }
      };
    }
  }


}
