import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SteganographieComponent } from './steganographie.component';

describe('SteganographieComponent', () => {
  let component: SteganographieComponent;
  let fixture: ComponentFixture<SteganographieComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SteganographieComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SteganographieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
