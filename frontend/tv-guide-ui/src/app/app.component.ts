import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TvGuideHeaderComponent} from "./tv-guide-header/tv-guide-header.component";
import {TvGuideFooterComponent} from "./tv-guide-footer/tv-guide-footer.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TvGuideHeaderComponent, TvGuideFooterComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'tv-guide-ui';
}
