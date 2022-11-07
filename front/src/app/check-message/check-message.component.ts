import { Component, OnInit } from '@angular/core';
import { Message } from '../classes/message';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-check-message',
  templateUrl: './check-message.component.html',
  styleUrls: ['./check-message.component.css']
})
export class CheckMessageComponent implements OnInit {

  constructor(private msgService : MessageService) { }

  ngOnInit(): void {
    this.getUserMessages();
  }
  Message:Message[]=[];
  test:Message={
    id:0,
    sent_to:"",
    owner:"",
    content:"",
    type_cryptage:"",
    para1:0,
    para2:0,

  }
  

// msg1:Message={sent_to:"",owner:"Moh",content:"Salut",type_cryptage:"gauche",para1:0,para2:0}
  getUserMessages():void{
    this.msgService.getUserMessages('Mohamed').subscribe(messages=>this.Message=messages);
  } 

  Decrypt(id:number):void{
    console.log(id)
    this.msgService.DecryptMessage(id).subscribe(message=>this.test=message);
    console.log("first")
    console.log(this.test)
    for (let i=0;i<this.Message.length;i++){
      if (this.test.id===this.Message[i].id)
      {this.Message[i].content=this.test.content}
      console.log('hi')
      console.log(this.Message[i])
    }


  
  }
}
