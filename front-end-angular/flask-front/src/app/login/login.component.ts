import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user-service';
import { AuthService } from '../services/auth-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public username: string ="";
  public password: string ="";
  constructor(public userService: UserService, public authService:AuthService, public route: Router) { }

  ngOnInit() {
  }

  login(){
      this.userService.login(this.username.toString(),this.password.toString()).subscribe(data => {
        this.authService.saveToken(data['access_token'], data['refresh_token'])
        this.route.navigate(['/main']);
      }, err => {
        alert("Something went wrong!");
      })
  }

}
