import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EncryptingComponent } from './encrypting.component';

describe('EncryptingComponent', () => {
  let component: EncryptingComponent;
  let fixture: ComponentFixture<EncryptingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EncryptingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EncryptingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
