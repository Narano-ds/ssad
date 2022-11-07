import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { User } from '../classes/user';
import { UserService } from '../user.service';
@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  constructor(private userService:UserService) { }
  public formData!: FormGroup;
  user:User={
    id:0,
    username:'',
    password:''
  }
  ngOnInit(): void {
    this.formData = new FormGroup({
      username:new FormControl('',Validators.required),
      password_hash:new FormControl('',Validators.required),
  
    })
  }
  
 Connect():void{
  this.userService.login(this.formData.value).subscribe(user=>this.user=user)

  console.log(this.user)
 }
}
