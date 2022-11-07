import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CheckMessageComponent } from './check-message/check-message.component';
import { EncryptingComponent } from './encrypting/encrypting.component';
import { HomeComponent } from './home/home.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { SteganographieComponent } from './steganographie/steganographie.component';

const routes: Routes = [{path:'',component: HomeComponent},
                        {path:'encrypt',component: EncryptingComponent,},
                        {path:'sign-up',component: SignUpComponent,},
                        {path:'sign-in',component: SignInComponent,},
                        {path:'check-message',component: CheckMessageComponent,},
                        {path:'stega',component: SteganographieComponent,}
                      ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents =[EncryptingComponent]