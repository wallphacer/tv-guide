import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentSearchBarComponent } from './content-search-bar.component';

describe('ContentSearchBarComponent', () => {
  let component: ContentSearchBarComponent;
  let fixture: ComponentFixture<ContentSearchBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContentSearchBarComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ContentSearchBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
