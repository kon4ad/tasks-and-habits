import { Injectable, NgModule } from "@angular/core";
import { LoginComponent } from "./login/login.component";
import { RegisterComponent } from "./register/register.component";
import { RouterModule } from '@angular/router';
import { MainPageComponent } from "./main-page/main-page.component";

const patches = [{path:'login', component: LoginComponent},
{path:'register', component:RegisterComponent}, {path:'main', component:MainPageComponent}]
 @NgModule ({
     imports: [RouterModule.forRoot(patches)],
     exports: [RouterModule]
 
 })
 export class MainRouter{}