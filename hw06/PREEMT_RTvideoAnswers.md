### Responses to Julia's video
**Where does Julia Cartwright work?**
National Instruments

**What is PREEMT_RT?**
It is a Linux patch that makes Linux into a real-time system

**What is mixed criticality?**
There is 2 different degrees of time sensitivity (one critical, one not)

**How can drivers misbehave?**
Since the driver stacks are shared between RT tasks and non-RT tasks, they may prioritize the non RT tasks.

**What is Δ in Figure 1?**
The time between an event is triggered and when it is actually executed

**What is Cyclictest[2]?**
Take a time stamp, sleep for a fixed duration and then sleep for a fixed duration. The difference between the two timestamps with the duration subtracted out is the delta mentioned above.

**What is plotted in Figure 2?**
A histogram of the Cyclictest being performed on an OS with and without the PREEMT_RT patch.

**What is dispatch latency? Scheduling latency?**
Dispatch: Amount of time it takes between the interrupt occurring and the thread scheduling being told something needs to run.
Scheduling: time it tasks from the scheduler running to the CPU being given the task to execute.

**What is mainline?**
Mainline tree is the tree where all new features are introduce d and developed
**What is keeping the External event in Figure 3 from starting?**
The execution of the low priority interrupt

**Why can the External event in Figure 4 start sooner?**
Using the PREEMT RT patch only a very small amount of time has to be spent waking up the threads. They can also now be preempted, reducing the irq_dispatch latency.