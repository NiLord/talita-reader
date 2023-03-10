import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProcessPdfService {

  constructor(private http: HttpClient) { }

  obtenerDatos(base64: any): Observable<any> {
    const data = {
      base64
    };
    return this.http.post<any>('http://nilord.com:5000/process-pdf', data);
  }
}
