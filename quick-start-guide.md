# TonUINO-TNG Control Reference Guide

## SD Card Setup

### SD Card Structure

The SD card must have the following structure:

```
SD Card Root/
├── mp3/           (system voice prompts - required)
├── advert/        (modifier announcements - required)
├── 01/            (your content folder 1)
│   ├── 0001.mp3
│   ├── 0002.mp3
│   └── ...
├── 02/            (your content folder 2)
│   ├── 0001.mp3
│   └── ...
├── 03/            (your content folder 3)
└── ...            (up to folder 99)
```

### Adding Your Audio Content

#### Step 1: Download System Files

Download the pre-configured system audio files from:  
[tonuino.github.io/TonUINO-TNG/sd-card.zip](https://tonuino.github.io/TonUINO-TNG/sd-card.zip)

Extract and copy the `mp3/` and `advert/` folders to your SD card root.

#### Step 2: Create Content Folders

1. Create numbered folders on your SD card: `01/`, `02/`, `03/`, etc. (up to `99/`)
2. Each folder can contain your music, stories, or audiobooks

#### Step 3: Add MP3 Files

**CRITICAL: File Naming Convention**

All MP3 files MUST use 4-digit zero-padded numbering:

✅ **CORRECT:**
- `0001.mp3`, `0002.mp3`, `0010.mp3`, `0099.mp3`, `0255.mp3`

❌ **WRONG:**
- `1.mp3`, `01.mp3`, `song.mp3`, `track_01.mp3`

**Examples:**

```
01/               (Folder for Album 1)
├── 0001.mp3     (Track 1)
├── 0002.mp3     (Track 2)
└── 0003.mp3     (Track 3)

02/               (Folder for Audiobook)
├── 0001.mp3     (Chapter 1)
├── 0002.mp3     (Chapter 2)
└── 0003.mp3     (Chapter 3)

03/               (Folder for Stories)
├── 0001.mp3
├── 0002.mp3
└── 0003.mp3
```

#### Language-Specific System Files

The repository includes pre-generated system audio in multiple languages:
- `sd-card-german/` - German voice prompts
- `sd-card-englisch/` - English voice prompts
- `sd-card-french/` - French voice prompts (if available)

Copy the appropriate language version to your SD card.

### System Audio Files Reference

- **`mp3/` folder** - System voice prompts for menu navigation, setup wizard, and instructions
- **`advert/` folder** - Modifier card announcements (freeze dance, sleep timer, etc.)

These folders contain 250+ pre-numbered system messages. Do not modify or remove these files unless you're creating custom voice prompts.

---

## Hardware Configuration

### Standard 3-Button Setup
- **A0 (Pin)**: Play/Pause Button
- **A1 (Pin)**: Up Button  
- **A2 (Pin)**: Down Button

### Default Card Behavior (pauseWhenCardRemoved = 1)

✓ **INSERT CARD** → Automatically starts playing  
✓ **REMOVE CARD** → Automatically pauses playback  
✓ **RE-INSERT SAME CARD** → Resumes from pause position  
✓ **INSERT DIFFERENT CARD** → Starts playing new card

> This makes TonUINO work like a music box - card on = play, card off = pause!

---

## Button Controls - 3 Buttons

### IDLE STATE (No card playing, device on)

| Button | Short Press | Long Press |
|--------|-------------|------------|
| Play/Pause | (none) | Enter Admin Menu (all 3 held) |
| Up | LED Brightness + | Shortcut 2 |
| Down | LED Brightness - | Shortcut 3 |
| Up + Down Together | (none) | Shortcut 1 (e.g., welcome sound) |

**⚡ DEFAULT BEHAVIOR (pauseWhenCardRemoved = 1)**
- Simply **PLACE A CARD** on the reader to start playing automatically
- No button press needed!

### PLAY STATE (Card is playing)

#### Normal Mode (invertVolumeButtons = 0)

| Button | Short Press | Long Press | Hold/Repeat |
|--------|-------------|------------|-------------|
| Play/Pause | Pause playback | Track number | - |
| Up | Next track | Volume up | Volume up |
| Down | Previous track | Volume down | Volume down |
| Up + Down Together | (none) | Jump to first | - |

#### Inverted Mode (invertVolumeButtons = 1)

| Button | Short Press | Long Press | Hold/Repeat |
|--------|-------------|------------|-------------|
| Play/Pause | Pause playback | Track number | - |
| Up | Volume up | Next track | - |
| Down | Volume down | Previous track | - |
| Up + Down Together | (none) | Jump to first | - |

### PAUSE STATE (Playback paused)

| Button | Short Press | Long Press |
|--------|-------------|------------|
| Play/Pause | Resume playback | Track number |
| Up | LED Brightness + | Shortcut 2 |
| Down | LED Brightness - | Shortcut 3 |
| Up + Down Together | (none) | Shortcut 1 |

**⚡ DEFAULT BEHAVIOR (pauseWhenCardRemoved = 1)**
- Card automatically **PAUSED** when removed from reader
- **PLACE SAME CARD** back on reader to resume playback
- **PLACE DIFFERENT CARD** to start playing new content
- No button press needed to resume!

### ADMIN MENU NAVIGATION

| Button | Short Press | Long Press |
|--------|-------------|------------|
| Play/Pause | Select/Confirm | Exit admin menu |
| Up | Next option (+1) | Next option (+10) |
| Down | Previous option (-1) | Previous option (-10) |

---

## Admin Menu Options

**Access Admin Menu:** Hold all 3 buttons together (or use admin card)

**Menu Options** (navigate with Up/Down, select with Play/Pause):

1. **Configure New Card** - Set up a blank or existing card
2. **Maximum Volume** - Set max speaker volume (0-30)
3. **Minimum Volume** - Set min speaker volume (0-30)
4. **Initial Volume** - Set startup volume
5. **EQ Settings** - Normal/Pop/Rock/Jazz/Classic/Bass
6. **Create Modifier Card** - Special behavior cards (see below)
7. **Configure Shortcut** - Assign folders to shortcuts 1-4
8. **Standby Timer** - Auto-shutdown: 5/15/30/60 min or disabled
9. **Create Cards for Folder** - Batch create single-track cards
10. **Invert Volume Buttons** - Swap volume/track navigation functions
11. **Reset All Settings** - Clear EEPROM (hold all buttons at startup)
12. **Lock Admin Menu** - Protect with: Off/Admin Card/PIN/Math
13. **Pause When Card Removed** - Enable/disable auto-pause on card removal
14. **Create Memory Game Cards** - Make cards for memory game (pairs)

---

## Card Registration Process (New Card)

### Automatic Detection

When an empty/unconfigured RFID card is detected:
1. System announces "Oh, a new card!" (t_300_new_tag)
2. Automatically enters card setup wizard
3. Follow the steps below

### Manual Setup via Admin Menu

1. Enter admin menu (hold all 3 buttons or use admin card)
2. Navigate to "1. Configure New Card"
3. Press Play/Pause to select
4. Remove admin card (if used)
5. Follow setup wizard below

### Card Setup Wizard - Step-by-Step

#### STEP 1: Select Playback Mode

**Prompt:** "Select playback mode" (t_310)  
Use Up/Down to choose from 14 modes:

1. **Admin Card** - Administrative functions access
2. **Repeat Last** - Replay last played content  
3. **Hörspiel (Audio Drama)** - Play all tracks, remember position
4. **Album** - Play all tracks in order
5. **Party** - Play tracks randomly (shuffle)
6. **Single Track (Einzel)** - Play one specific track
7. **Audiobook (Hörbuch)** - Play folder, save progress across power cycles
8. **Audio Drama From-To** - Play random track in range
9. **Album From-To** - Play tracks in range sequentially
10. **Party From-To** - Play tracks in range randomly
11. **Quiz Game** - Interactive quiz mode
12. **Memory Game** - Memory card matching game
13. **Bluetooth Toggle** - Switch Bluetooth module on/off
14. **Audiobook Single** - Single audiobook with track count

Press Play/Pause to confirm mode.

#### STEP 2: Select Folder (if applicable)

**Prompt:** "Select folder" (t_301)
- Navigate folders 1-99 with Up/Down
- System previews first track from selected folder
- Press Play/Pause to confirm
- **SKIPPED FOR:** Admin card, Repeat last, Bluetooth toggle

#### STEP 3: Mode-Specific Configuration

Depending on mode selected:

**For Single Track Mode:**
- **Prompt:** "Select file" (t_327)
- Choose specific track number (1-255)
- System previews the track
- Press Play/Pause to confirm

**For From-To Modes (Audio Drama/Album/Party):**
- **Prompt:** "Select first file" (t_328)
  - Choose starting track
  - Press Play/Pause to confirm
- **Prompt:** "Select last file" (t_329)
  - Choose ending track
  - Press Play/Pause to confirm

**For Quiz Mode:**
- **Prompt:** "How many different answers?" (t_333)
- Options:
  - 2 answers
  - 4 answers
  - 2 answers + 1 solution
  - 4 answers + 1 solution
  - Only solution with buzzer

**For Audiobook Single Mode:**
- **Prompt:** "Select number of tracks"
- Choose how many tracks in audiobook
- Press Play/Pause to confirm

**Announce Track Numbers?** (for certain modes):
- **Prompt:** "Say number before each file?" (t_330)
- Options:
  - No (t_331)
  - Yes (t_332)

#### STEP 4: Write to Card

1. System prompts: "Please put the card on now!" (t_800)
2. Place RFID card on reader
3. System writes configuration data
   - **SUCCESS:** "OK" sound (t_400)
   - **ERROR:** Error sound (t_401)
4. System prompts: "Remove card from reader!" (t_801)
5. Remove card
6. Card is now configured and ready to use!

---

## Modifier Cards (Special)

Modifier cards change TonUINO behavior. Place **AFTER** a music card to activate.

### Available Modifiers

1. **Sleep Timer** - Auto-shutdown timer (5/15/30/60 minutes)
2. **Freeze Dance** - Random pause game (stop dance)
3. **Fire Water Air** - Physical activity game
4. **Toddler Mode** - Lock all buttons (cards still work)
5. **Kindergarten Mode** - No new cards until current song ends
6. **Repeat Single Track** - Endless loop of current track
7. **Bluetooth Toggle** - Switch Bluetooth on/off
8. **Jukebox Mode** - Queue cards instead of interrupting
9. **Pause After Track** - Auto-pause after each track
10. **Disable Standby** - Temporarily disable standby timer

---

## Shortcuts (1-4)

Shortcuts trigger without a card (from Idle/Pause state).

### Shortcut Triggers

- **Shortcut 1:** Long press Up + Down together
- **Shortcut 2:** Long press Up
- **Shortcut 3:** Long press Down  
- **Shortcut 4:** On startup (via GPIO pin, if configured)

### Configuration

Via Admin Menu → Option 7 → Choose shortcut → Setup like normal card

### Use Cases

- Welcome sound on startup (Shortcut 4)
- Quick access to favorite albums (1-3)
- Goodnight playlist/meditation sounds

---

## Batch Card Creation Features

### Create Cards for Folder (Admin Menu #9)

Create multiple single-track cards for one folder at once.

**Process:**
1. Select folder via setup wizard
2. Choose first track number
3. Choose last track number
4. System prompts for each card sequentially
5. Place blank card → System writes → Remove card → Repeat
6. Long press Play/Pause to exit early

### Create Memory Game Cards (Admin Menu #14)

Create numbered cards for memory game matching pairs.

**Process:**
1. System announces card number to create
2. Use Up/Down to change card number (+/-1, +/-10)
3. Place blank card → System writes → Remove card
4. Press Play/Pause when done with all cards

---

## Special Card Behaviors

### Card Insertion Behavior

**⚡ DEFAULT: "pauseWhenCardRemoved = 1" (ENABLED)**  
This is the music box behavior - configured by default!

✓ **INSERT CARD** → Starts playing automatically (no button needed)  
✓ **REMOVE CARD** → PAUSES playback automatically  
✓ **RE-INSERT SAME CARD** → RESUMES from pause position (no button needed)  
✓ **INSERT NEW CARD** → Starts playing the new card

**ALTERNATE: "pauseWhenCardRemoved = 0" (DISABLED)**  
Can be changed via Admin Menu → Option 13

- Insert card → Starts playing
- Remove card → Playback CONTINUES (does not pause)
- Re-insert any card → Starts that card (interrupts current playback)

### Admin Card

Special configuration card that opens admin menu when detected.
- One admin card can be configured at setup
- Used to access admin functions without holding all buttons
- Can be re-learned via Admin Menu Lock settings

### Resume on Same RFID (enabled by default)

If the same card that started playback is detected again:
- In Pause state: Resumes playback
- In Play state: (ignored by default with RESUME_ON_SAME_RFID)

---

## Playback Mode Behaviors

### Mode Details

- **Hörspiel (Audio Drama):** Plays all, remembers position in EEPROM
- **Album:** Plays all tracks sequentially, no memory
- **Party:** Random shuffle of all tracks
- **Single Track:** Plays one specific track only
- **Audiobook (Hörbuch):** Saves progress after each track
- **Audio Drama/Album/Party VB:** "Von-Bis" (From-To) with track range
- **Quiz Game:** Interactive quiz with answer buttons
- **Memory Game:** Matching card pairs game
- **Bluetooth Toggle:** Switch BT module on/off
- **Repeat Last:** Replays previous card/shortcut

---

## Technical Information

### Card Data Structure

Each RFID card stores:
- **Cookie:** 0x1337B347 (verification signature)
- **Version:** 2 (card format version)
- **Folder:** 1-99 (or 0 for special functions)
- **Mode:** Playback mode (1-14)
- **Special:** Mode-specific data (track #, start track, timer, etc.)
- **Special2:** Additional mode data (end track, options, etc.)

### Supported RFID Cards

- MIFARE Classic 1K
- MIFARE Classic 4K  
- MIFARE Ultralight
- NTAG213/215/216

### Storage Locations (EEPROM)

- **0-99:** Folder progress (audiobook positions)
- **100-140:** Admin settings (41 bytes)
- **141-155:** Reserved (15 bytes)
- **156-255:** Extra shortcuts (100 bytes, max 25 shortcuts)

---

## Troubleshooting

### Card Not Detected
- Ensure card is placed flat on reader for 1-2 seconds
- Check MFRC522 wiring and power
- Verify card is supported MIFARE/NTAG type

### Card Plays Wrong Content
- May be configured for different folder
- Re-configure via Admin Menu → Option 1

### Buttons Not Responding
- Check if Toddler Mode modifier is active (remove modifier card)
- Check if Kindergarten Mode is active
- Verify button wiring to A0, A1, A2

### Volume/Navigation Swapped
- Check "Invert Volume Buttons" setting (Admin Menu #10)
- Toggle to switch between modes

### Device Shuts Down Unexpectedly
- Check Standby Timer setting (Admin Menu #8)
- Check Sleep Timer modifier card
- Verify battery voltage (if battery powered) 