import { Component, OnInit, Input } from '@angular/core';
import { Task } from '../task-list.component';

@Component({
  selector: 'app-task-label',
  templateUrl: './task-label.component.html',
  styleUrls: ['./task-label.component.css']
})
export class TaskLabelComponent implements OnInit {
  @Input() label: string;
  @Input() tasks: Task[];
  public tasksDone: Task[];
  public tasksUndone: Task[];
  public showDone:boolean = false;
  constructor() { }

  ngOnInit() {
    this.tasksDone = new Array();
    this.tasksUndone = new Array();
    this.tasks.forEach(task => {
      if(task.is_done){
        this.tasksDone.push(task)
      }else {
        this.tasksUndone.push(task)
      }
    })
    this.tasksDone.reverse();
    this.tasksUndone.reverse();
  }

  doneUndone(){
    this.showDone = !this.showDone;
  }
}
