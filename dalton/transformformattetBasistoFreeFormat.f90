PROGRAM CHANGEBASIS
implicit none
integer LUBAS2,LUBAS,LUPRI,IOSTAT,IOS,L
character(len=140) :: STRING,FILENAME
CHARACTER(len=1)    :: SIGN
integer :: nExponential, nOrbitals
logical :: READSTRING
LOGICAL       :: BLANK,READCOEF,segmentedFormat
LUBAS2=1
open( unit=LUBAS2, file='transformAll.sh' ,status="old")
FILENAME(1:11)='           '
FULLOOP: DO 
   READ(LUBAS2,'(A140)')FILENAME
   IF(FILENAME(1:11).EQ.'END OF FILE')EXIT
!   print*,'FILENAME',FILENAME
!   IF(FILENAME(1:9).EQ.'Huckel')THEN
      LUBAS=3
      open( unit=LUBAS, file=TRIM(FILENAME),status="old")      
      LUPRI=4
      open( unit=LUPRI, file=TRIM(FILENAME)//'NEW',status="replace")
      READSTRING = .TRUE.
      FILELOOP: DO
         IF(READSTRING)READ(LUBAS,'(A140)', IOSTAT=ios) STRING
         IF(IOS.LT.0) EXIT FILELOOP
         IF(READSTRING)CALL WRITE_STRING(LUPRI,STRING)
         READSTRING = .TRUE.
         READ (STRING, '(A1)') SIGN
         IF ((SIGN .EQ. 'a') .OR. (SIGN .EQ. 'A')) THEN
            CHARGELOOP: DO
               READ(LUBAS,'(A140)', IOSTAT=ios) STRING
               IF(IOS.LT.0) EXIT FILELOOP
               CALL WRITE_STRING(LUPRI,STRING)
               READ (STRING, '(A1)') SIGN
               IF (SIGN .EQ. ' ') THEN
                  CALL TEST_BLANK_LINE(BLANK, STRING)
                  IF (BLANK) THEN
                     cycle CHARGELOOP
                  ELSE
                     READCOEF=.TRUE.
                  ENDIF
               ELSEIF((SIGN .EQ. 'a') .OR. (SIGN .EQ. 'A')) THEN
                  !done with this charge
                  READSTRING=.FALSE.
                  EXIT CHARGELOOP
               ELSEIF(SIGN .EQ. '$') THEN !Comment line
                  cycle CHARGELOOP
               ENDIF
               IF(READCOEF)THEN
                  READ (STRING,*) nExponential, nOrbitals
                  segmentedFormat = nOrbitals.EQ. 0
                  IF (segmentedFormat) nOrbitals = nExponential
                  IF(nExponential .NE. 0)THEN
                     CALL CHANGEBASISSETFORCHARGE(LUBAS,LUPRI,nExponential,nOrbitals,segmentedFormat)                     
                  ENDIF
                  READCOEF=.FALSE.
               ENDIF
            ENDDO CHARGELOOP
         ELSEIF(SIGN .EQ. '$') THEN !Comment line
            cycle FILELOOP
         ENDIF
      ENDDO FILELOOP
      close(unit=LUPRI)
      close(unit=LUBAS)
!   ENDIF
ENDDO FULLOOP

close(unit=LUBAS2)

CONTAINS
  SUBROUTINE WRITE_STRING(LUPRI,STRING)
    implicit none
    integer :: lupri
    character(len=140) :: STRING
    integer :: L
    CHARACTER(len=4)    :: FORM4
    CHARACTER(len=5)    :: FORM5
    CHARACTER(len=6)    :: FORM6
    L = LEN(TRIM(STRING))
    IF(L.LT.1000.AND.L.GE.100)THEN
       WRITE(FORM6,'(A2,I3,A1)') '(A',L,')'
       WRITE(LUPRI,FORM6) STRING
    ELSEIF(L.LT.100.AND.L.GE.10)THEN
       WRITE(FORM5,'(A2,I2,A1)') '(A',L,')'
       WRITE(LUPRI,FORM5) STRING
    ELSEIF(L.LT.10)THEN
       WRITE(FORM4,'(A2,I1,A1)') '(A',L,')'
       WRITE(LUPRI,FORM4) STRING
    ENDIF
  END SUBROUTINE WRITE_STRING

SUBROUTINE CHANGEBASISSETFORCHARGE(LUBAS,LUPRI,nprim,nOrbital,segmentedFormat)
implicit none
integer :: lupri,lubas,nExponential
INTEGER, PARAMETER :: realk = 8
real(realk) :: Exp,CC(10000)
character(len=140) :: STRING
INTEGER               :: ios,IEX,I,M,IPRINT
LOGICAL               :: POLFUN,CONTRACTED,segmentedFormat,BLANK
INTEGER               :: atype,nang,nprim,nOrbital,NUMNUMOLD
INTEGER               :: J,NUMBER_OF_LINES,KNTORB,NUMNUM,KAUG,nNumbers
J = 0
DO WHILE( J .LT. nprim) 
   READ(LUBAS, '(A140)', IOSTAT = IOS) STRING
   IF(ios /= 0)THEN
      WRITE (LUPRI,'(2A)') ' Error in basisset file1'
      STOP 'Error in basisset file1'
   ELSE
      READ (STRING, '(A1)') SIGN
      IF (SIGN .EQ. ' ') THEN
         CALL TEST_BLANK_LINE(BLANK, STRING)
         IF (.NOT. BLANK) THEN
            !We have found a line with a primitive and some coeffecients
            J=J+1 
            CALL LINES_OF_CONTRACTION(nOrbital, NUMBER_OF_LINES,segmentedFormat)
            IF (NUMBER_OF_LINES .EQ. 1) THEN
               KNTORB = nOrbital
            ELSE
               KNTORB = 6
            END IF
            IF(segmentedFormat)THEN
               KNTORB = 1
            ENDIF
            !         Reading the first line with exponents and contractioncoeffecients
            READ (STRING,'(F16.9, 6F12.9)') Exp,&
                 &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)

            IF (segmentedFormat)THEN
               CC(J)=1.0E0_realk
            ENDIF
                IF(EXP.LT.1000000)THEN 
               WRITE(LUPRI,'(1X,F16.9,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.10000000)THEN 
               WRITE(LUPRI,'(1X,F16.8,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.100000000)THEN 
               WRITE(LUPRI,'(1X,F16.7,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.1000000000)THEN 
               WRITE(LUPRI,'(1X,F16.6,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.10000000000)THEN 
               WRITE(LUPRI,'(1X,F16.5,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.100000000000)THEN 
               WRITE(LUPRI,'(1X,F16.4,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.1000000000000)THEN 
               WRITE(LUPRI,'(1X,F16.3,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.10000000000000)THEN 
               WRITE(LUPRI,'(1X,F16.2,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSEIF(EXP.LT.100000000000000)THEN 
               WRITE(LUPRI,'(1X,F16.1,6(1X,F13.9))')Exp,&
                    &(CC(J+(I-1)*(nprim)),I = 1, KNTORB)
            ELSE
               STOP 'ERROR EXP TOO LARGE'
            ENDIF
            !         If there are more lines with contraction-coeffecients
            !         they will be read here.
            DO I=2, NUMBER_OF_LINES
               NUMNUM = 6 + (I-1)*7
               !Getting the format for the read-stat right.
               KNTORB = MIN(NUMNUM, nOrbital)
               !Making the usual safety-precautions before we read the 
               !contraction-coeffecients.
               READ(LUBAS, '(A140)', IOSTAT = IOS) STRING
               IF(ios /= 0)THEN
                  WRITE (LUPRI,'(2A)') ' Error in basisset file2'
                  STOP 'Error in basisset file2'
               ELSE
                  READ (STRING, '(A1)') SIGN
                  IF (SIGN .EQ. ' ') THEN
                     CALL TEST_BLANK_LINE(BLANK, STRING)
                     IF (.NOT. BLANK) THEN
                        !We now have a line with contraction-coeffecients.
                        READ (STRING,'(F16.9,6F12.9)')&
                             &(CC(J+(M-1)*(nprim)),&
                             & M = 6 + (I-2)*7 +1, KNTORB)
                        WRITE(LUPRI,'(4X,7(1X,F13.9))')&
                             &(CC(J+(M-1)*(nprim)),&
                             & M = 6 + (I-2)*7 +1, KNTORB)
                     END IF
                  ELSE
                     cycle
                  ENDIF
               ENDIF
            ENDDO
         ENDIF
      ENDIF
   ENDIF
ENDDO
END SUBROUTINE CHANGEBASISSETFORCHARGE

SUBROUTINE LINES_OF_CONTRACTION(nOrbital, NUMBER_OF_LINES,segmentedFormat)
!*********************************************************************
!* CALCULATE ON HOW MANY LINES THE CONTRACTION COEFFICIENTS ARE 
!* WRITTEN ON
!*********************************************************************
implicit none
INTEGER     :: NUMBER_OF_LINES,nOrbital
INTEGER, PARAMETER :: realk = 8
REAL(realk) :: B,C
LOGICAL     :: segmentedFormat
!The intrisic functions DBLE makes a souble precision reak number of an integer.
IF (segmentedFormat) THEN
  NUMBER_OF_LINES = 1
  RETURN
ENDIF
B = DBLE(7)
C = DBLE(nOrbital) - DBLE(6) 
! This finds out how many lines we have, and puts it into NUMBER_OF_LINES.
      IF ((nOrbital - 6) .LE. 0) THEN
         NUMBER_OF_LINES = 1
      ELSE IF (DMOD(C,B) .LT. 1.0E-30_realk) THEN
         NUMBER_OF_LINES = (nOrbital - 6)/7 + 1
      ELSE
         NUMBER_OF_LINES = (nOrbital - 6)/7 + 2
      END IF
END SUBROUTINE LINES_OF_CONTRACTION

SUBROUTINE TEST_BLANK_LINE(BLANK, STRING)
!**********************************************************************
!* TEST IF THE STRING IS BLANK
!*********************************************************************
implicit none
CHARACTER*(*) :: STRING
LOGICAL       :: BLANK
INTEGER       :: J
BLANK = .TRUE.
DO J = 1, LEN(STRING)
   BLANK = BLANK .AND. (STRING(J:J) .EQ. ' ')
ENDDO
END SUBROUTINE TEST_BLANK_LINE
END PROGRAM CHANGEBASIS

