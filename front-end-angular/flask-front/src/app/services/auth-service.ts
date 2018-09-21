import { Injectable } from "@angular/core";
import { Router } from "@angular/router";
import { HttpHeaders, HttpClient } from "@angular/common/http";
import { CookieService } from 'ngx-cookie-service';
import { UserService } from "./user-service";

@Injectable()
export class AuthService {
  constructor(
    public _router: Router, public _http: HttpClient, public cookie: CookieService){}
   
  saveToken(tokenacc, tokenreff){
    var expireDate = 5/(24*60);
    this.cookie.set("access_token", tokenacc, expireDate, "/");
    this.cookie.set("refresh_token", tokenreff, expireDate+5, "/");
  }
 
  getHeader() : HttpHeaders{
    var headers = new HttpHeaders({'Accept': 'application/json', 'Authorization': 'Bearer '+this.cookie.get('access_token')});
    return headers;
  }
 
  isLogged():boolean{
    if (!this.cookie.check('access_token')){
        if(this.cookie.check('refresh_token')){
          let get = this._http.get("http://localhost:5000/token/refresh", {headers: new HttpHeaders({'Accept': 'application/json', 'Authorization': 'Bearer '+this.cookie.get('refresh_token')})})
          get.subscribe(token => {
            this.saveToken(token['access_token'],this.cookie.get('refresh_token'))
            return true;
          })
        }else {
          return false;
        }
        return false;
    }else {
        return true;
    }
  } 
 
  logout() {
    this.cookie.set("access_token", '', new Date("Thu, 01 Jan 1970 00:00:01 GMT"),"/");
    this.cookie.set("refresh_token", '', new Date("Thu, 01 Jan 1970 00:00:01 GMT"),"/");
    this.cookie.deleteAll('../', "/");
    this._router.navigate(['/login']);
  } 


}