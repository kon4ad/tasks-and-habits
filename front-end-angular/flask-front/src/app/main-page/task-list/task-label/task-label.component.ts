import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-task-label',
  templateUrl: './task-label.component.html',
  styleUrls: ['./task-label.component.css']
})
export class TaskLabelComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}

export interface Task {
  label:string;
  task_desc: string;
  time_created: any;
  is_done: boolean;
  end_time: any;
}