import { Component, OnInit, Input } from '@angular/core';
import { Task } from '../../task-list.component';
import { UserService } from '../../../../services/user-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-task-item',
  templateUrl: './task-item.component.html',
  styleUrls: ['./task-item.component.css']
})
export class TaskItemComponent implements OnInit {
  @Input() task: Task;
  public showMenu: boolean = false;
  constructor(public userService: UserService,public router: Router) { }

  ngOnInit() {
  }

  show() {
    this.showMenu = !this.showMenu;
  }

  goEdit(){
    this.router.navigate(['edit', this.task.id]);
  }

  markAsDone(){
    this.userService.markAsDone(this.task.id).subscribe(resp => {
      this.userService.emitter.emit("updated");
    })

  }

  delete() {
    this.userService.deleteTask(this.task.id).subscribe(resp => {
      this.userService.emitter.emit("deleted");
    })
  }

}
