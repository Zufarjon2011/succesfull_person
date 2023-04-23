from mcpi.minecraft import Minecraft
from time import sleep

# Connect to the Minecraft game
mc = Minecraft.create()

# Get the player's position
pos = mc.player.getTilePos()

# Set the block type and place it at the player's position
mc.setBlock(pos.x, pos.y, pos.z, 1)

# Wait for 5 seconds
sleep(5)

# Set the block type to air to remove it
mc.setBlock(pos.x, pos.y, pos.z, 0)