import { Message } from '../classes/message';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { MessageService } from '../message.service';
@Component({
  selector: 'app-encrypting',
  templateUrl: './encrypting.component.html',
  styleUrls: ['./encrypting.component.css']
})
export class EncryptingComponent implements OnInit {
  public formData!: FormGroup;
  constructor(private messageService:MessageService) { }
  message : Message={
    id:0,
    sent_to:"",
    owner:"",
    content:"",
    type_cryptage:"gauche",
    para1:0,
    para2:0

  }
  direction:string='';
  changeMethod(value:string){
    console.log(value);
    this.message.type_cryptage=value;
    if(value =='Cesare' || value =='Decalage'){this.cond2=true}
    
    console.log(this.cond2)
  }
  changeDirection(value:string){
    this.direction=value;
    console.log(this.direction);
  }

  ngOnInit(): void {
    this.formData = new FormGroup({
      sent_to:new FormControl('',Validators.required),
      owner:new FormControl('presentation'),
      content:new FormControl('',Validators.required),
      para1:new FormControl('0'),
      para2:new FormControl(''),
      type_cryptage:new FormControl('')

  
    })
  }
  cond2=false;

  send_request(){
    
    this.formData.patchValue({
      type_cryptage:this.message.type_cryptage,
    })
    if (this.message.type_cryptage=="Decalage")
    {
      this.formData.patchValue({
        type_cryptage:this.direction,

      })
    }
    //console.log(this.formData.value)
     this.messageService.send_post_request(this.formData.value).subscribe();

  }

}
