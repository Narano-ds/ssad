import { HttpHeaders,HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { Message } from './classes/message';

@Injectable({
  providedIn: 'root'
})
export class MessageService {

  constructor(private http:HttpClient) { }

  private _refresh = new Subject<void>();
  private MessageURL='http://127.0.0.1:5000/api/messages'
  private MessageURL2='http://127.0.0.1:5000/api/messages/GetbyUsername'
  private MessageURL3='http://127.0.0.1:5000/api/messages//DecryptMessage/'

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  get refresh(){
    return this._refresh;
  }

  send_post_request(message:Message){
    return this.http.post(this.MessageURL,message,this.httpOptions);
  }
  getUserMessages(user:string):Observable<Message[]>{
    const url = `${this.MessageURL2}/${user}`;
    return this.http.get<Message[]>(url)
  }
  DecryptMessage(id:number):Observable<Message>{
    const url = `${this.MessageURL3}/${id}`;
    return this.http.get<Message>(url)
  }

}
