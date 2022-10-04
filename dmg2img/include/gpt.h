#define GPT_HDR_SIG "EFI PART"
#define GPT_HDR_REVISION 0x00010000

#define GPT_ENT_TYPE_UNUSED \
        {0x00000000,0x0000,0x0000,0x00,0x00,{0x00,0x00,0x00,0x00,0x00,0x00}}
#define GPT_ENT_TYPE_EFI \
        {0xc12a7328,0xf81f,0x11d2,0xba,0x4b,{0x00,0xa0,0xc9,0x3e,0xc9,0x3b}}
#define GPT_ENT_TYPE_MBR \
        {0x024dee41,0x33e7,0x11d3,0x9d,0x69,{0x00,0x08,0xc7,0x81,0xf3,0x9f}}
#define GPT_ENT_TYPE_HFSPLUS \
        {0x48465300,0x0000,0x11aa,0xaa,0x11,{0x00,0x30,0x65,0x43,0xec,0xac}}
#define GPT_ENT_TYPE_APPLEUFS \
        {0x55465300,0x0000,0x11aa,0xaa,0x11,{0x00,0x30,0x65,0x43,0xec,0xac}}
#define GPT_ENT_TYPE_ZFS \
        {0x6a898cc3,0x1dd2,0x11b2,0x99,0xa6,{0x08,0x00,0x20,0x73,0x66,0x31}}

#define GPT_ENT_TYPE_MS_RESERVED \
        {0xe3c9e316,0x0b5c,0x4db8,0x81,0x7d,{0xf9,0x2d,0xf0,0x02,0x15,0xae}}
#define GPT_ENT_TYPE_MS_BASIC_DATA \
        {0xebd0a0a2,0xb9e5,0x4433,0x87,0xc0,{0x68,0xb6,0xb7,0x26,0x99,0xc7}}
#define GPT_ENT_TYPE_MS_LDM_METADATA \
        {0x5808c8aa,0x7e8f,0x42e0,0x85,0xd2,{0xe1,0xe9,0x04,0x34,0xcf,0xb3}}
#define GPT_ENT_TYPE_MS_LDM_DATA \
        {0xaf9b60a0,0x1431,0x4f62,0xbc,0x68,{0x33,0x11,0x71,0x4a,0x69,0xad}}

struct _guid {
	uint32_t time_low;
	uint16_t time_mid;
	uint16_t time_hi_and_version;
	uint8_t clock_seq_hi_and_reserved;
	uint8_t clock_seq_low;
	uint8_t node[6];
}     __attribute__((__packed__));

struct _gpt_header {
	char hdr_sig[8];
	uint32_t hdr_revision;
	uint32_t hdr_size;
	uint32_t hdr_crc_self;
	uint32_t __reserved;
	uint64_t hdr_lba_self;
	uint64_t hdr_lba_backup;
	uint64_t hdr_lba_start;
	uint64_t hdr_lba_end;
	struct _guid hdr_guid;
	uint64_t hdr_lba_table;
	uint32_t hdr_entries;
	uint32_t hdr_entsz;
	uint32_t hdr_crc_table;
	uint32_t padding;
}           __attribute__((__packed__));

struct _gpt_entry {
	struct _guid ent_type;
	struct _guid ent_guid;
	uint64_t ent_lba_start;
	uint64_t ent_lba_end;
	uint64_t ent_attr;
	uint16_t name[36];	/* UTF-16 */
}          __attribute__((__packed__));