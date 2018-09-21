import { Injectable, NgModule } from "@angular/core";
import { LoginComponent } from "./login/login.component";
import { RegisterComponent } from "./register/register.component";
import { RouterModule } from '@angular/router';
import { MainPageComponent } from "./main-page/main-page.component";
import { MainGuard } from "./guard";
import { EditTaskComponent } from "./edit-task/edit-task.component";

const patches = [{path:'login', component: LoginComponent},
{path:'register', component:RegisterComponent}, {path:'main', component:MainPageComponent, canActivate:[MainGuard]},
{path:'edit/:id', component:EditTaskComponent, canActivate:[MainGuard]}]
 @NgModule ({
     imports: [RouterModule.forRoot(patches)],
     exports: [RouterModule]
 
 })
 export class MainRouter{}