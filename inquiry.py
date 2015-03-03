from ctypes import *
"""
typedef struct sg_io_hdr
{
    int interface_id;           /* [i] 'S' for SCSI generic (required) */
    int dxfer_direction;        /* [i] data transfer direction  */
    unsigned char cmd_len;      /* [i] SCSI command length ( <= 16 bytes) */
    unsigned char mx_sb_len;    /* [i] max length to write to sbp */
    unsigned short iovec_count; /* [i] 0 implies no scatter gather */
    unsigned int dxfer_len;     /* [i] byte count of data transfer */
    void * dxferp;              /* [i] [*io] points to data transfer memory or
                                             scatter gather list */
    unsigned char * cmdp;       /* [i] [*i] points to SCSI command to perform */
    unsigned char * sbp;        /* [i] [*o] points to sense_buffer memory */
    unsigned int timeout;       /* [i] MAX_UINT->no timeout (unit: millisec) */
    unsigned int flags;         /* [i] 0 -> default, see SG_FLAG... */
    int pack_id;                /* [i->o] unused internally (normally) */
    void * usr_ptr;             /* [i->o] unused internally */
    unsigned char status;       /* [o] scsi status */
    unsigned char masked_status;/* [o] shifted, masked scsi status */
    unsigned char msg_status;   /* [o] messaging level data (optional) */
    unsigned char sb_len_wr;    /* [o] byte count actually written to sbp */
    unsigned short host_status; /* [o] errors from host adapter */
    unsigned short driver_status;/* [o] errors from software driver */
    int resid;                  /* [o] dxfer_len - actual_transferred */
    unsigned int duration;      /* [o] time taken (unit: millisec) */
    unsigned int info;          /* [o] auxiliary information */
} sg_io_hdr_t;  /* around 64 bytes long (on i386) */
"""
import pdb
pdb.set_trace()
class SgIoHdr(Structure):
     _fields_ = [("interface_id",c_ubyte),
                 ("dxfer_direction",c_int),
		 ("cmd_len",c_ubyte),
		("mx_sb_len",c_ubyte),
		("iovec_count", c_ushort),
		("dxfer_len", c_uint),
		#("dxferp",c_void_p),
		("cmdp",c_char_p)]
'''		("sbp",POINTER(c_char)),
		("timeout",c_uint ),
		("flags", c_uint),
		("pack_id", c_int),
		("usr_ptr", c_void_p),
		("status", c_ubyte),
		("masked_status", c_ubyte),
		("msg_status", c_ubyte),
		("sb_len_wr",c_ubyte ),	
		("host_status",c_ushort ),
		("driver_status", c_ushort),
		("resid",c_int ),
		("duration",c_uint ),
		("info",c_uint)]'''


diskname=(c_ubyte * 20)()
INQ_REPLY_LEN = 96
INQ_CMD_CODE = 0x12
INQ_CMD_LEN = 6
SG_DXFER_NONE=-1,
SG_DXFER_TO_DEV=-2,
SG_DXFER_FROM_DEV=-3,
SG_DXFER_TO_FROM_DEV=-4

#diskname = raw_input('Enter a disk name: ')
diskname="/dev/sg2"
inqCmdBlk = (c_ubyte * INQ_CMD_LEN)(INQ_CMD_CODE, 0, 0, 0, INQ_REPLY_LEN, 0)
cmd=cast(inqCmdBlk,c_char_p)
inqBuff = (c_ubyte * INQ_REPLY_LEN)


sense_buffer = (c_ubyte * 32)()
print type(sense_buffer)


sg_fd=c_int()
k=c_int()
status=c_int()



io_hdr=SgIoHdr(interface_id='S',
	       cmd_len = sizeof(inqCmdBlk),
	       iovec_count = 0,
    	       mx_sb_len = sizeof(sense_buffer),
    	       dxfer_direction = SG_DXFER_FROM_DEV,
    	       dxfer_len = INQ_REPLY_LEN,
    	       #dxferp = inqBuff,
   	       cmdp = cmd)
'''    	       sbp = sense_buffer)
    	       timeout = 20000,  
    	       flags = 0,
    	       pack_id = 0,
    	       usr_ptr = None)'''

print io_hdr.interface_id

import pdb
#pdb.set_trace()
print diskname

'''
libinquiry = cdll.LoadLibrary('./libinquiry.so.1.0')

sg_inquiry=libinquiry.sg_inquiry
sg_inquiry.argtypes = (DefaultCStruct,POINTER(c_char))
sg_inquiry.restype = c_int

sg_inquiry(SgIoHdr,diskname)
'''



