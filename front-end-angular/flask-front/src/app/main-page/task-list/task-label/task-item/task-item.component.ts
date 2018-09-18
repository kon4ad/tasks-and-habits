import { Component, OnInit, Input } from '@angular/core';
import { Task } from '../../task-list.component';

@Component({
  selector: 'app-task-item',
  templateUrl: './task-item.component.html',
  styleUrls: ['./task-item.component.css']
})
export class TaskItemComponent implements OnInit {
  @Input() task: Task;
  public showMenu: boolean = false;
  constructor() { }

  ngOnInit() {
  }

  show() {
    this.showMenu = !this.showMenu;
  }

}
