import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule, routingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { EncryptingComponent } from './encrypting/encrypting.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ReactiveFormsModule } from '@angular/forms';
import { SignInComponent } from './sign-in/sign-in.component';
import { CheckMessageComponent } from './check-message/check-message.component';
import { SteganographieComponent } from './steganographie/steganographie.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    EncryptingComponent,
    SignUpComponent,
    SignInComponent,
    CheckMessageComponent,
    SteganographieComponent
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }


