import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserService } from '../../services/user-service';

@Component({
  selector: 'app-adding-new-task',
  templateUrl: './adding-new-task.component.html',
  styleUrls: ['./adding-new-task.component.css']
})
export class AddingNewTaskComponent implements OnInit {
  public label: string;
  public taskText: string;

  constructor(public userService: UserService) { }

  ngOnInit() {
  }

  addTask(){
    this.userService.addTask({label: this.label, task_desc: this.taskText}).subscribe(resp => {
      console.log(resp);
    })
  }

}
