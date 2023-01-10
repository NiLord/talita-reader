import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PdfUpdateComponent } from './pdf-update.component';

describe('PdfUpdateComponent', () => {
  let component: PdfUpdateComponent;
  let fixture: ComponentFixture<PdfUpdateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PdfUpdateComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PdfUpdateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
