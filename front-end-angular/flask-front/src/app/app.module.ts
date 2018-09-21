import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { MainPageComponent } from './main-page/main-page.component';
import { MainRouter } from './app-router';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { UserService } from './services/user-service';
import { AuthService } from './services/auth-service';
import { CookieService } from 'ngx-cookie-service';
import { AddingNewTaskComponent } from './main-page/adding-new-task/adding-new-task.component';
import { TaskListComponent } from './main-page/task-list/task-list.component';
import { TaskLabelComponent } from './main-page/task-list/task-label/task-label.component';
import { TaskItemComponent } from './main-page/task-list/task-label/task-item/task-item.component';
import { MainGuard } from './guard';
import { NavbarComponent } from './navbar/navbar.component';
import { EditTaskComponent } from './edit-task/edit-task.component';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    MainPageComponent,
    AddingNewTaskComponent,
    TaskListComponent,
    TaskLabelComponent,
    TaskItemComponent,
    NavbarComponent,
    EditTaskComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserModule,
    RouterModule,
    MainRouter,
 
  ],
  providers: [UserService, CookieService ,AuthService, MainGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
