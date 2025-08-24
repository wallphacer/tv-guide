import { Component } from '@angular/core';
import {ContentSearchBarComponent} from "../content-search-bar/content-search-bar.component";

@Component({
  selector: 'app-tv-guide-header',
  standalone: true,
  imports: [
    ContentSearchBarComponent
  ],
  templateUrl: './tv-guide-header.component.html',
  styleUrl: './tv-guide-header.component.css'
})
export class TvGuideHeaderComponent {

}
