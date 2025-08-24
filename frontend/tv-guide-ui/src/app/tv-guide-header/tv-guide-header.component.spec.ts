import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TvGuideHeaderComponent } from './tv-guide-header.component';

describe('TvGuideHeaderComponent', () => {
  let component: TvGuideHeaderComponent;
  let fixture: ComponentFixture<TvGuideHeaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TvGuideHeaderComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TvGuideHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
