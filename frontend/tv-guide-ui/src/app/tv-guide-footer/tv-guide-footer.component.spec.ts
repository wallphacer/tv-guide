import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TvGuideFooterComponent } from './tv-guide-footer.component';

describe('TvGuideFooterComponent', () => {
  let component: TvGuideFooterComponent;
  let fixture: ComponentFixture<TvGuideFooterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TvGuideFooterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TvGuideFooterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
