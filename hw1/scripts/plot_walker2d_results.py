import matplotlib.pyplot as plt

num_steps = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
bc_mean = [716.991, 475.710, 1077.006, 3889.276, 4362.744, 1368.754, 4485.238, 4123.062, 2473.817, 4727.592]
percent_expert = [0.13, 0.09, 0.20, 0.72, 0.81, 0.25, 0.83, 0.77, 0.46, 0.88]

fig, ax1 = plt.subplots(figsize=(8,5))

color = 'tab:blue'
ax1.set_xlabel('num_agent_train_steps_per_iter')
ax1.set_ylabel('BC Mean', color=color)
ax1.plot(num_steps, bc_mean, marker='o', color=color, label='BC Mean')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Percentage of Expert', color=color)
ax2.plot(num_steps, percent_expert, marker='s', color=color, label='Percentage of Expert')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Walker2d-v4: BC Mean and Percentage of Expert vs Training Steps')
plt.savefig('walker2d_bc_results.png')
plt.close()
