import { Component } from '@angular/core';
import {ContentSearchBarComponent} from "../content-search-bar/content-search-bar.component";

@Component({
  selector: 'app-tv-guide-footer',
  standalone: true,
    imports: [
        ContentSearchBarComponent
    ],
  templateUrl: './tv-guide-footer.component.html',
  styleUrl: './tv-guide-footer.component.css'
})
export class TvGuideFooterComponent {

}
