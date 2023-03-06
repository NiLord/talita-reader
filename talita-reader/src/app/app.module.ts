import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PdfUpdateComponent } from './pdf-update/pdf-update.component';
import { HttpClientModule } from '@angular/common/http';
import { ToFixedPipe } from './round.pipe';

@NgModule({
  declarations: [
    AppComponent,
    PdfUpdateComponent,
    ToFixedPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
