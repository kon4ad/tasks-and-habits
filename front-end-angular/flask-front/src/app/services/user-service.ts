import { Injectable, EventEmitter } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { AuthService } from "./auth-service";
import { Task } from "../main-page/task-list/task-list.component";

@Injectable()
export class UserService {
    public emitter: EventEmitter<String> = new EventEmitter();
    constructor(public http: HttpClient, public auth: AuthService){}

    login(username: string, password: string){
        return this.http.post("http://localhost:5000/login", {"username": username, "password": password})
    }

    register(username: string, password: string){
        return this.http.post("http://localhost:5000/register", {"username": username, "password": password})
    }

    addTask(task){
        return this.http.post("http://localhost:5000/task/add", task, {headers: this.auth.getHeader()})
    }

    getTask(id:number){
        return this.http.get<Task[]>("http://localhost:5000/task/get/"+id, {headers: this.auth.getHeader()});
    }
    updateTask(task: Task){
        return this.http.post("http://localhost:5000/task/update", task, {headers: this.auth.getHeader()})
    }

    getTasks() {
        return this.http.get<Task[]>("http://localhost:5000/task/get/all", {headers: this.auth.getHeader()})
    }

    deleteTask(id:number) {
        return this.http.delete("http://localhost:5000/task/delete/"+id, {headers: this.auth.getHeader()})
    }

    markAsDone(id:number){
        return this.http.get("http://localhost:5000/task/mark/oposite/"+id, {headers: this.auth.getHeader()})
    }
}