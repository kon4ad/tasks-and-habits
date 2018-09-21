import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user-service';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {

  public tasksMap: Map<string,Task[]>;
  constructor(public userService: UserService) { }

  ngOnInit() {
    this.userService.emitter.subscribe(data => {
      
      this.init();
    })
    this.init();
    console.log(this.tasksMap)
  }
  init() {
    this.tasksMap = new Map();
    this.userService.getTasks().subscribe(tasks => {
      tasks.forEach(task => {
        if(!this.tasksMap.has(task.label)){
          let taskArr = new Array();
          taskArr.push(task);
          this.tasksMap.set(task.label, taskArr);
        }else {
          let taskArr = this.tasksMap.get(task.label);
          taskArr.push(task);
          this.tasksMap.set(task.label, taskArr)
        }
      })
    })

  }
  getKeys(map){
    let listLabels =  Array.from(map.keys());
    let listSpliceMap = new Array()
    listSpliceMap.push(listLabels.slice(0,listLabels.length/2))
    listSpliceMap.push(listLabels.slice(listLabels.length/2, listLabels.length))
    return listSpliceMap;
  }


}

export interface Task {
  id:number;
  label:string;
  task_desc: string;
  time_created: any;
  is_done: boolean;
  end_time: any;
}