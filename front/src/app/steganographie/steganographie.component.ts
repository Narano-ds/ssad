import { Component, OnInit } from '@angular/core';
import { MessageService } from '../message.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-steganographie',
  templateUrl: './steganographie.component.html',
  styleUrls: ['./steganographie.component.css']
})
export class SteganographieComponent implements OnInit {
  public formData!: FormGroup;
  constructor(private msgService:MessageService) { }
  ngOnInit(): void {
    this.formData = new FormGroup({
      sent_to:new FormControl('',Validators.required),
      owner:new FormControl('presentation'),
      content:new FormControl('',Validators.required),
      para1:new FormControl('0'),
      para2:new FormControl(''),
      type_cryptage:new FormControl('steganographie')

  
    })


}

send_request(){
    

  //console.log(this.formData.value)
   this.msgService.send_post_request(this.formData.value).subscribe();

}
}
