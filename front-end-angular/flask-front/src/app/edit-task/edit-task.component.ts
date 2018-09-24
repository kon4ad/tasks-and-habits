import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../services/user-service';
import { Task } from '../main-page/task-list/task-list.component';

@Component({
  selector: 'app-edit-task',
  templateUrl: './edit-task.component.html',
  styleUrls: ['./edit-task.component.css']
})
export class EditTaskComponent implements OnInit, OnDestroy {

  id: number;
  private sub: any;
  public task:Task;
  selectTask = "T";
  constructor(private route: ActivatedRoute, public users: UserService, public router: Router) {}

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
       this.id = +params['id']; 
       this.users.getTask(this.id).subscribe(task => {
        this.task = task[0];

       })
    });
  }

  editTask(){
    let acu = this.task.end_time
    this.task.end_time = new Date(this.task.end_time).getTime();
    this.users.updateTask(this.task).subscribe(resp => {
      this.router.navigate(['main'])
    })
    this.task.end_time = acu;
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
