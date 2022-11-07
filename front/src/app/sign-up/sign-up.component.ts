import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  public formData!: FormGroup;
  constructor(private userService:UserService) { }

  ngOnInit() {
    this.formData = new FormGroup({
    username:new FormControl('',Validators.required),
    password_hash:new FormControl('',Validators.required),

  })
  }



  send_request():void{
    // console.log(this.formData)
    this.userService.send_post_request(this.formData.value).subscribe();
  }
}
