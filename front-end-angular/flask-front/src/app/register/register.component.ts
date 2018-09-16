import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user-service';
import { AuthService } from '../services/auth-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  public username: string ="";
  public password: string ="";
  public repassword: string="";
  constructor(public userService: UserService, public authService:AuthService, public route: Router) { }

  ngOnInit() {
    //this.register()
  }

  register(){
    if(this.repassword == this.password){
      this.userService.register(this.username.toString(),this.password.toString()).subscribe(data => {
        this.authService.saveToken(data['access_token'], data['refresh_token'])
        alert("You has been registered!")
        this.route.navigate(['/main'])
      }, err => {
        alert("Something went wrong!");
      })
    }else {
      alert("password have to match!")
      this.password="";
      this.repassword="";
    }

  }

}
