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
  constructor() { }

  ngOnInit() {
  }

}
