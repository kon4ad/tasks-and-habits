import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user-service';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {

  public taskLabels: string[];
  constructor(public userService: UserService) { }

  ngOnInit() {
    this.userService.getTasks().subscribe(tasks => {
      
    })
  }
}

export interface Task {
  label:string;
  task_desc: string;
  time_created: any;
  is_done: boolean;
  end_time: any;
}