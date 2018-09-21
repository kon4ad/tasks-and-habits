import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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
  constructor(private route: ActivatedRoute, public users: UserService) {}

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
       this.id = +params['id']; 
       this.users.getTask(this.id).subscribe(task => {
        this.task = task[0];
       })
    });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
