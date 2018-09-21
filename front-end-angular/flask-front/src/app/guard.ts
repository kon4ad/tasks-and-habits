import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from "@angular/router";
import { Observable } from "rxjs/Observable";
import { Injectable } from "@angular/core";
import { AuthService } from "./services/auth-service";

@Injectable()
export class MainGuard implements CanActivate {
    constructor(public auth:AuthService){}
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | Observable<boolean> | Promise<boolean> {
     return this.auth.isLogged();
    }
}