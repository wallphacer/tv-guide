import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayResultsAreaComponent } from './display-results-area.component';

describe('DisplayResultsAreaComponent', () => {
  let component: DisplayResultsAreaComponent;
  let fixture: ComponentFixture<DisplayResultsAreaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DisplayResultsAreaComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DisplayResultsAreaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
