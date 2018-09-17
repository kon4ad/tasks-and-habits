import { Component, OnInit, EventEmitter } from '@angular/core';
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
  public selectTask: any = "T"
  public selectHabit: any = "D"
  public endTime:any;
  constructor(public userService: UserService) { }

  ngOnInit() {
  }

  addTask(){
    let date = new Date(this.endTime);
    this.userService.addTask({label: this.label, task_desc: this.taskText, end_time: date.getTime()}).subscribe(resp => {
      console.log(resp);
      this.userService.emitter.emit("reload")
    })
  }

}
