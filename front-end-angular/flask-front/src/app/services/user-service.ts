import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable()
export class UserService {

    constructor(public http: HttpClient){}

    login(username: string, password: string){
        return this.http.post("http://localhost:5000/login", {"username": username, "password": password})
    }

    register(username: string, password: string){
        return this.http.post("http://localhost:5000/register", {"username": username, "password": password})
    }
}