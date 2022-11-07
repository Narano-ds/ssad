import { Injectable } from '@angular/core';
import { User } from './classes/user';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http:HttpClient) { }


  private userURL='http://127.0.0.1:5000/api/users'
  private userURL2='http://127.0.0.1:5000/api/users/Login'

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  send_post_request(user:User){
    return this.http.post(this.userURL,user,this.httpOptions);
  }

  login(user:User):Observable<User>{
    // const url = `${this.userURL}/${user}`;
    let params1 = new HttpParams().set(user.username,user.password)
    return this.http.get<User>(this.userURL2,{params:params1})

  }


}
